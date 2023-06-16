Task 1) Lockbox.
Look at the LockBox class in e5utils.py. It is constructed with a password and contents. The contents are confidential, and they should only be revealed to a user who knows the password. The try_password method allows a user to attempt using a single password. If the correct password is provided, then the method returns the contents. Otherwise, it returns None. All passwords will use only lowercase ASCII characters.

You are an attacker. You must implement break_lockbox in breaking.py. Given a LockBox, it should return a tuple (password, contents) containing the password and contents of the lockbox. You may only call the try_password method of LockBox. You may not access its fields. The fields of LockBox will be renamed and additional fields added during testing. Attempting to brute force the answer will not work, so instead ask yourself, is there any indication when you discover one additional correct character?

You can find an example test for break_lockbox in test_breaking.py. You can run the tests with pytest in CSIL. You should be able to break a 10 character password in 15 seconds on a CSIL desktop machine. You must be able to break a 10 character password in 30 seconds to receive credit. Notice that this precludes brute forcing. NOTE: You will want to log into the desktop machines (even remotely) because they have more consistent timing behavior.

Question.
How would you modify LockBox to prevent this attack?

Task 2) Welcoming a takeover.
Look at the Facade and CaerfilyDesinedSurvis classes in e5utils.py. A CaerfilyDesinedSurvis service executes a string of commands given to it by clients like Facade and returns results. A service is created with a codeword that can be used to gain access to additional (privileged) commands. Each command produces a single string as output, and the outputs of all commands in a string are returned in order in a list. Specifically, there are 3 commands:

greet <name>. This command takes one argument (a name) and greets the person with that name. The command returns a string like "Hi <name>".
dumpcodeword. This command dumps the codeword of the service. It returns that codeword as a string.
takeover <passcode>. This command simulates taking over the service. It takes a single argument, a codeword. If the codeword is the same one that the service was created with, then it is assumed that the user is privileged, and the takeover() method of the service is called. It returns a special string indicating that the service was taken over. If the codeword does not match the codeword of the service, then the takeover fails and a failure message is returned.
You are an attacker. You must implement break_facade in breaking.py. Given a Facade, it should find a way to call the takeover() method of the Facades creating service and return the resulting message. It must do this by invoking greet() on the Facade. You may not directly access the fields of the Facade or directly call methods of the service.

You can find an example test for break_facade in test_breaking.py.

Question.
How would you modify Facade and CaerfilyDesinedSurvis to prevent this attack?
