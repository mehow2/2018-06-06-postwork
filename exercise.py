import cmd
import sys
import turtle


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    f = None
    filename = './commands.cmd'

    # ----- basic turtle commands -----
    def do_record(self):
        self.record = True

    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        turtle.forward(int(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        turtle.right(int(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        turtle.left(int(arg))

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        turtle.home()

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        turtle.circle(int(arg))

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())

    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    def do_record(self, arg):
        self.f = open(self.filename, 'w')

    def do_playback(self, arg):
        if not self.f:
            with open(self.filename, 'r') as f:
                self.cmdqueue.extend(f.read().splitlines())

    def do_stop(self, arg):
        if self.f:
            self.f.close()
            self.f = None

    def precmd(self, line):
        line = line.lower()
        if self.f and 'playback' not in line:
            print(line, file=self.f)
        return line


if __name__ == '__main__':
    TurtleShell().cmdloop()
