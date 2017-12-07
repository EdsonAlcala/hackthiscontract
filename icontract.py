class IContract:
    def __init__(self):
        self.contract_address = None
        self.user_address = None

    '''Performs any operations needed after the contract has been deployed'''

    def setup(self):
        raise NotImplementedError("setup is not implemented!")

    '''Returns true if the contract has been hacked, false otherwise'''
    def has_been_hacked(self):
        raise NotImplementedError("perform_validation is not implemented!")
