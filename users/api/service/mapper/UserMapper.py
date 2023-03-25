from users.api.service.dtos.UserDTO import UserDTO
from users.domain.User import User


class UserMapper:

    @staticmethod
    def toDTO(user):
        if user is None:
            return None
        else:
            return UserDTO(user.userId, user.name, user.lastName, user.password, user.email, user.isConnected)

    @staticmethod
    def toEntity(createUserDTO):
        return User(createUserDTO.name, createUserDTO.lastName, createUserDTO.password, createUserDTO.email,
                    createUserDTO.isConnected)

