So i finished the netcat replacements section with some of my own improvement.

1. The server died when entering empty string into buffer. Fixed by checking if the buffer is empty with if statement.
2. The server kept dying when entering a command not known. Fixed by adding an except block "FileNotFoundError"
3. Added some more graceful exits as it bugs me..

Although. I cannot get the server to gracefully exit the "def listen(self)" function after a client has connected. Something with the threading is messing it up.
Thoughts?

