from aws_cdk import CfnTag

def MyTags(tagmap: any):
    tags=None
    if tagmap is not None:
        tags=[]
        for key,value in tagmap.items():
            tags.append(CfnTag(key=key,value=value))
    return tags
