from __future__ import annotations
from typing import Optional, Sequence, MutableSequence


class LockBox:
    def __init__(self, password: str, contents: str):
        self.__secret_password = password
        self.__secret_contents = contents
        self.secret_hash = 0

    # Given a string password, returns:
    #  * The secret contents when the given password matches the secret password
    #  * None when the given password does not match the secret password
    def try_password(self, password: str) -> Optional[str]:
        secret_hash = 3
        local_password = self.__secret_password

        for i in range(min(len(password), len(local_password))):
            if password[i] != local_password[i]:
                return None

            for j in range(200 + 200*i):
                secret_hash += 1
            
            secret_hash *= secret_hash
            secret_hash %= 7
            secret_hash += 1
        
        if len(password) != len(local_password):
            return None

        self.secret_hash = secret_hash
        return self.__secret_contents


class Facade:
    def __init__(self, service: CaerfilyDesinedSurvis):
        self.__service = service
      
    def greet(self, name: str) -> MutableSequence[str]:
        command = 'greet {}'.format(name)
        return self.__service.execute(command)


class CaerfilyDesinedSurvis:
    def __init__(self, admin_codeword: str):
        self.__admin_codeword = admin_codeword
        
    def create_facade(self):
        return Facade(self)

    def takeover(self) -> str:
        return 'Taking over!'

    def execute(self, commands: str) -> Sequence[str]:
        results: MutableSequence[str] = []
        for line in commands.splitlines():
            tokens = line.split()
            command = tokens[0]
            args = tokens[1:]
            
            if command == 'greet':
                results.append('Hello, {}'.format(args[0]))

            elif command == 'dumpcodeword':
                results.append(self.__admin_codeword)
                
            elif command == 'takeover':
                if args[0] == self.__admin_codeword:
                    results.append(self.takeover())
                else:
                    results.append('You are not strong enough to take over')

        return results
           
