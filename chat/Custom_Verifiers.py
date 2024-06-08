from .models import OTP,User


class Otp_verify:
    " Verifies a given OTP"
    def __init__(self,otp):
        self.otp = otp

    def is_valid(self):
        "Returns True and set self.user if otp is valid otherwise False"
        otp_ref = OTP.objects.get(otp=self.otp)

        if User.objects.filter(email=otp_ref.email).exists():
            user_ref = User.objects.get(email=otp_ref.email)
            self.user = user_ref
            return True
        return False
    
    def get_user(self):
        "Returns the user associated with the given otp otherwise a warning message"
        if self.user:
            return self.user
        return """ No User found, Please make sure you called is_valid or the otp is correct.
                 """