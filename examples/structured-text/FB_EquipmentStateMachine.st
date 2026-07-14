FUNCTION_BLOCK FB_EquipmentStateMachine
VAR_INPUT
    bEnableRequest : BOOL;
    bStartEdge : BOOL;
    bStopRequest : BOOL;
    bStopComplete : BOOL;
    bMotionAllowed : BOOL;
    bFaultActive : BOOL;
    bResetEdge : BOOL;
END_VAR
VAR_OUTPUT
    eState : E_EquipmentState := E_EquipmentState.IDLE;
    bRunCommand : BOOL;
END_VAR

bRunCommand := FALSE;

IF bFaultActive AND (eState <> E_EquipmentState.FAULT) THEN
    eState := E_EquipmentState.FAULT;
END_IF

CASE eState OF
    E_EquipmentState.IDLE:
        IF bEnableRequest AND bMotionAllowed THEN
            eState := E_EquipmentState.READY;
        END_IF

    E_EquipmentState.READY:
        IF bStartEdge AND bMotionAllowed THEN
            eState := E_EquipmentState.RUNNING;
        END_IF

    E_EquipmentState.RUNNING:
        bRunCommand := bMotionAllowed;
        IF (NOT bMotionAllowed) OR bFaultActive THEN
            eState := E_EquipmentState.FAULT;
        ELSIF bStopRequest THEN
            eState := E_EquipmentState.STOPPING;
        END_IF

    E_EquipmentState.STOPPING:
        IF bStopComplete THEN
            eState := E_EquipmentState.READY;
        END_IF

    E_EquipmentState.FAULT:
        IF bResetEdge AND (NOT bFaultActive) THEN
            eState := E_EquipmentState.RESETTING;
        END_IF

    E_EquipmentState.RESETTING:
        eState := E_EquipmentState.IDLE;
END_CASE
