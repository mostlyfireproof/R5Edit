""" Store long strings and Squirrel functions here to avoid cluttering main.py """

CREATEPROPFUNCTION = '''
#if SERVER
entity function CreateEditorProp(asset a, vector pos, vector ang, bool mantle = false, float fade = 2000)
{
	entity e = CreatePropDynamic(a,pos,ang,SOLID_VPHYSICS,fade)
	e.kv.fadedist = fade
	if(mantle) e.AllowMantle()
	return e
}
#endif

'''

HEADER = '''
#if SERVER
void function SpawnEditorProps()
{
    // Written by mostly fireproof. Let me know if there are any issues!
'''

FOOTER = '''
}
#endif
'''