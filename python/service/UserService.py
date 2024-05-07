from pojo.User import User
from config.databaseConnect import Session


class UserService:
    def __init__(self):
        self.session = Session()

    def findAll(self):
        users = self.session.query(User).all()
        users_role = []
        for user in users:
            if user.role == 'wurt':
                user.role = '沃特'
            if user.role == 'wickerbottom':
                user.role = "威克巴顿"
            if user.role == 'default':
                user.role = "尚未选择"
            if user.role == 'wanda':
                user.role = "旺达"
            if user.role == 'wortox':
                user.role = "沃托克斯"
            if user.role == 'waxwell':
                user.role = '麦斯威尔'
            if user.role == 'woodie':
                user.role = '吴迪'
            if user.role == 'wx78':
                user.role = 'wx-78'
            users_role.append(user.role)
        return users_role


