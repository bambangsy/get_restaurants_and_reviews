
def parsegeo(link):
    link = link
    indexaw = link.find("/@")
    indexak = link.find("/data")
    geo_and_scale = link[indexaw+2:indexak]
    parse = geo_and_scale.split(",")
    geo = parse[0]+","+parse[1]
    return geo

    

    
