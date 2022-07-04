// See https://aka.ms/new-console-template for more information
using System.Text.Json;
// if(!Directory.Exists("Texture"))
//     Directory.CreateDirectory("Texture");

// if(!Directory.Exists("USD"))
//     Directory.CreateDirectory("USD");

//step2 copy texture
void updataFiles(string dir,string destdir,List<string> filter)
{
    DirectoryInfo dirinfo = new(dir);
    if(dirinfo.Exists)
    {
        foreach(FileInfo i in dirinfo.EnumerateFiles())
        {
            if(filter.Contains(Path.GetExtension(i.Name)))
            {
                File.Copy(i.FullName,Path.Combine(destdir,i.Name),true);
            }
        }
    }
}


if(File.Exists("config.json"))
{
    string a=File.ReadAllText("config.json",System.Text.Encoding.UTF8);
    QN.AssetData? b = JsonSerializer.Deserialize<QN.AssetData>(a);
    if(b != null)
    {
        if(b.type=="Asset")
        {
            if(!Directory.Exists("Texture"))
                Directory.CreateDirectory("Texture");

            if(!Directory.Exists("USD"))
                Directory.CreateDirectory("USD");
            
            if(!Directory.Exists("Upper/MOD"))
                Directory.CreateDirectory("Upper/MOD");

            if(!Directory.Exists("Upper/TEX"))
                Directory.CreateDirectory("Upper/TEX");
            
            updataFiles(Path.Combine(b.directory.asset,"Texture"),"Texture",new List<string>{".tx"});
            updataFiles(b.directory.tex_maya,"Upper/TEX",new List<string>{".ma",".mb"});
            updataFiles(b.directory.tex_usd,"Upper/TEX",new List<string>{".usd"});
            updataFiles(b.directory.mod_usd,"Upper/MOD",new List<string>{".usd"});
        }
        else
        {
            Console.WriteLine("配置文件不匹配");
        }
        
    }
    
}
else
{
    Console.WriteLine("缺少配置文件");
}

