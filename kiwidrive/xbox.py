class XboxController:
    def __init__(self, joystick):
        self.joystick = joystick

    BUTTON_A = 1
    BUTTON_B = 2
    BUTTON_X = 3
    BUTTON_Y = 4
    BUTTON_BUMP_LEFT = 5
    BUTTON_BUMP_RIGHT = 6
    BUTTON_BACK = 7
    BUTTON_START = 8
    BUTTON_JOY_LEFT = 9
    BUTTON_JOY_RIGHT = 10

    JOY_STICK_L_X = 0
    JOY_STICK_L_Y = 1
    JOY_TRIG_L = 2
    JOY_TRIG_R = 3
    JOY_STICK_R_X = 4
    JOY_STICK_R_Y = 5

    def digital_claw(self):
        return self.joystick.getRawButton(XboxController.BUTTON_A)

    def analog_drive_x(self):
        return self.joystick.getRawAxis(XboxController.JOY_STICK_L_X)

    def analog_drive_y(self):
        return self.joystick.getRawAxis(XboxController.JOY_STICK_L_Y)

    def analog_rot(self):
        return self.joystick.getRawButton(XboxController.BUTTON_BUMP_RIGHT) -\
               self.joystick.getRawButton(XboxController.BUTTON_BUMP_LEFT)

    def analog_winch(self):
        return self.joystick.getRawJoy(XboxController.JOY_TRIG_R) -\
               self.joystick.getRawJoy(XboxController.JOY_TRIG_L)

    def analog_arm(self):
        return self.joystick.getRawButton(XboxController.BUTTON_Y) -\
               self.joystick.getRawButton(XboxController.BUTTON_B)

    def digital_test(self):
        return self.joystick.getRawButton(XboxController.BUTTON_BACK)

    def digital_winch_encoder_reset(self):
        return self.joystick.GetRawButton(XboxController.BUTTON_START)

    def digital_winch_override(self):
        return self.joystick.GetRawButton(XboxController.BUTTON_X)

    def A(self):
        return self.joystick.getRawButton(1)

    def B(self):
        return self.joystick.getRawButton(2)

    def X(self):
        return self.joystick.getRawButton(3)

    def Y(self):
        return self.joystick.getRawButton(4)

    def left_bump(self):
        return self.joystick.getRawButton(5)

    def right_bump(self):
        return self.joystick.getRawButton(6)

    def back(self):
        return self.joystick.getRawButton(7)

    def start(self):
        return self.joystick.getRawButton(8)

    def left_joystick_down(self):
        return self.joystick.getRawButton(9)

    def right_joystick_down(self):
        return self.joystick.getRawButton(10)

    def left_joystick_axis_h(self):
        return self.joystick.getRawAxis(0)

    def left_joystick_axis_v(self):
        return self.joystick.getRawAxis(1)

    def right_joystick_axis_h(self):
        return self.joystick.getRawAxis(4)

    def right_joystick_axis_v(self):
        return self.joystick.getRawAxis(5)

    def right_trigger(self):
        return self.joystick.getRawAxis(3)

    def left_trigger(self):
        return self.joystick.getRawAxis(2)

    def d_pad(self):
        return self.joystick.getPOV()
