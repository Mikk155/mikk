import mikk

number = "1.1234567";

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_1 )
print( f"1 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_2 )
print( f"2 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_3 )
print( f"3 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_4 )
print( f"4 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_5 )
print( f"5 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.digits_6 )
print( f"6 digit {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.integer )
print( f"integer {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.integer_round_up )
print( f"integer round UP {str1}" );

str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.integer_round_down )
print( f"integer round DOWN {str1}" );

number = "1.1000000";
str1 = mikk.fmt.float( number, mikk.fmt.FloatConversion.not_zero )
print( f"integer Non-zero decimals {str1}" );
