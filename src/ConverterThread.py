import os
from threading import Thread


class ConverterThread(Thread):
    def __init__(self, converter):
        super().__init__()
        # Need reference to converter to be able to change GUI items:
        self.converter = converter

    def run(self):
        # Create '.tmp' directory:
        if not os.path.exists('.tmp'):
            os.mkdir('.tmp')

        # Create string for commands:
        to_write = ''
        if self.converter.application.invert:
            to_write += 'invert true\n'
        to_write += 'folder\n'
        to_write += self.converter.selected_folder[1:] + '\n'
        to_write += 'converter\nload\n'
        to_write += 'width ' + str(self.converter.width) + '\n'
        to_write += 'convert\n'

        # Write commands file:
        with open('.tmp/input', mode='w', encoding='utf-8') as file:
            file.write(to_write)

        # Run generator with created input:
        if not os.path.exists('generator'):
            self.info_label = 'Generator executable not found. Have you built this project correctly?\n'
        os.system('./generator <.tmp/input 1>.tmp/output 2>.tmp/error')

        if not os.path.exists('.tmp/output'):
            os.error('Output not created')

        # Read the generator output and get the info from it:
        output_str = ''
        with open('.tmp/output', mode='r', encoding='utf-8') as file:
            output_str = file.read()
        lines = output_str.split('\n')
        k = -4
        line = lines[k]
        output_str = ''
        while 'Convert' in line:
            if 'Converted' in line:
                output_str += line + '\n'
            k -= 1
            line = lines[k]
        self.converter.info_label = output_str

        # Remove temporary stuff:
        os.remove('.tmp/input')
        os.remove('.tmp/output')
        os.remove('.tmp/error')
        os.removedirs('.tmp')