import pexpect

password_prompt = ''
password = ''

child = pexpect.spawn('kinit')
child.expect(password_prompt)
child.sendline(password)
child.send('\n')