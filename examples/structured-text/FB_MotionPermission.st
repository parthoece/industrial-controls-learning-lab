FUNCTION_BLOCK FB_MotionPermission
VAR_INPUT
    bEmergencyStopReleased : BOOL;
    bGuardClosed : BOOL;
    bNetworkHealthy : BOOL;
    bDriveFault : BOOL;
    bExternalPermission : BOOL;
END_VAR
VAR_OUTPUT
    bMotionAllowed : BOOL;
    eBlockReason : E_MotionBlockReason;
END_VAR

bMotionAllowed := FALSE;
eBlockReason := E_MotionBlockReason.NONE;

IF NOT bEmergencyStopReleased THEN
    eBlockReason := E_MotionBlockReason.EMERGENCY_STOP_ACTIVE;
ELSIF NOT bGuardClosed THEN
    eBlockReason := E_MotionBlockReason.GUARD_OPEN;
ELSIF NOT bNetworkHealthy THEN
    eBlockReason := E_MotionBlockReason.NETWORK_UNHEALTHY;
ELSIF bDriveFault THEN
    eBlockReason := E_MotionBlockReason.DRIVE_FAULT;
ELSIF NOT bExternalPermission THEN
    eBlockReason := E_MotionBlockReason.EXTERNAL_PERMISSION_MISSING;
ELSE
    bMotionAllowed := TRUE;
END_IF
