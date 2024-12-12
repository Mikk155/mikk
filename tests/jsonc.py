import os
import mikk

mikk.LoggerLevel.set( mikk.LoggerLevel.warning | mikk.LoggerLevel.debug );

json = mikk.jsonc.load( os.path.join( os.path.dirname(__file__), "jsonc.json" ) );
print( json );

json = mikk.jsonc.load( os.path.join( os.path.dirname(__file__), "unexistent-json.json" ), except_ok=True );
print( json );
