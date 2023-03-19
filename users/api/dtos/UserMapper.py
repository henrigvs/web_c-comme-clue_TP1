from users.api.dtos.UserDTO import UserDTO
from users.domain.User import user


class UserMapper:

    @staticmethod
    def toDTO(user):
        if user:
            return UserDTO(user.name, user.lastName,  user.password, user.email)
        else:
            return None

    @staticmethod
    def toEntity(userDTO):
        return user(userDTO.name, userDTO.lastName, userDTO.password, userDTO.email)
