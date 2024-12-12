import mikk

mikk.LoggerLevel.set( mikk.LoggerLevel.warning );
str1 = mikk.g_Logger.warn( "Global message as {}", "str1" );

class YourCustomClass:
    m_Logger = mikk.Logger( "My Custom Class" );
str2 = YourCustomClass.m_Logger.warn( "Message for my custom class as {}", "str2" );

mikk.LoggerLevel.clear( mikk.LoggerLevel.warning );
str2 = YourCustomClass.m_Logger.warn( "This message won't display but well print it anways" );
print(str2)
