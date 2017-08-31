import parsekit
class SaveName(parsekit.Step):
    firstname = parsekit.Argument("Your first name", required=True, type=str)
    def run(self, record, metadata):
        metadata['firstname'] = self.options.firstname
        self.log.info(metadata)
        return record, metadata

class SayHello(parsekit.Step):
    def run(self, input_, metadata):
        self.log.info("Hello " + metadata['firstname'])
        return input_, metadata
