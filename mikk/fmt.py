"""
The MIT License (MIT)

Copyright (c) 2024 Mikk155

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

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

    @staticmethod
    def join( directory: str ) -> str:

        '''
        Returns the absolute path to the provided directory

        **directory**: Path starting from the workspace the main script was called.
        '''

        from os.path import abspath;
        from os.path import join;

        __destination__ = abspath( '' );

        __directories__ = directory.split( '/' );

        for __dir__ in __directories__:

            __dir__ = __dir__.strip();

            if __dir__:

                __destination__ = join( __destination__, __dir__ );

        return __destination__;

    @staticmethod
    def listdict( list: list, index_key: bool = False, value_int: bool = False ) -> dict[str, str] | dict[str, int]:
        '''
        Formats a list into a dictionary passing indexes as either keys or values

        ``index_key`` if True the index will be formated as keys, if False as values

        ``value_int`` if ``index_key`` is False and this is True, the values will be int, otherwise str
        '''

        data: dict = {};

        for index, item in enumerate( list ):

            if index_key:

                data[ str(index) ] = item;

            elif value_int:
                
                data[ item ] = index;

            else:

                data[ item ] = str(index);

        return data;
