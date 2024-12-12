class fmt:
    '''
    All about formatting
    '''

    @staticmethod
    def format( string: str, *args ) -> str:

        '''
        Formats the given ``string`` replacing brackets for arguments in ``args``
        '''

        for arg in args:

            string = string.replace( "{}", arg, 1 );

        return string;