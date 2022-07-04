
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
using System.Collections.Generic;
namespace QN;
public class Project
{
    [JsonPropertyName("id")]
    public string id {get;set;}

    [JsonPropertyName("project.database")]
    public string  database {get;set;}

    [JsonPropertyName("project.entity")]
    public string  entity {get;set;}

    [JsonPropertyName("project.full_name")]
    public string  full_name {get;set;}

    [JsonPropertyName("project.template")]
    public string  template {get;set;}
    
}

public class Asset
{
    [JsonPropertyName("id")]
    public string id {get;set;}

    [JsonPropertyName("asset.cn_name")]
    public string cn_name {get;set;}

    [JsonPropertyName("asset.entity")]
    public string entity {get;set;}

    [JsonPropertyName("asset.link_asset_type")]
    public string link_asset_type {get;set;}
}


public class Directory
{
    [JsonPropertyName("id")]
    public string id {get;set;}

    [JsonPropertyName("asset")]
    public string asset {get;set;}

    [JsonPropertyName("tex_maya")]
    public string tex_maya {get;set;}

    [JsonPropertyName("tex_abc")]
    public string tex_abc {get;set;}

    [JsonPropertyName("mod_abc")]
    public string mod_abc {get;set;}

    
}
public class Link
{
    [JsonPropertyName("id")]
    public string id {get;set;}

    [JsonPropertyName("asset")]
    public string asset {get;set;}

}

public class Scene
{
    public Asset asset {get;set;}
    public Directory directory {get;set;}
}
public class AssetData
{
    public string type {get;set;}
    public Project project {get;set;}
    
    public List<Scene> scenes {get;set;} = new();
    
    public List<Link> links{get;set;}
}