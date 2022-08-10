#pragma once
//#include "stagetool.h"
#include <vector>
#include <string>
#include <iostream>
#include <map>
int main(int argc,char** argv)
{
	//std::map<std::string, std::string> images;
	//std::vector<std::string> images;
	//std::vector<std::string> colorspace;
	//GetAssetTexture("D:/test/test2/maya3.usda",images);
	//std::pair<const std::string, const std::string> i;
	/*for (int i =0 ;i<images.size();i++)
	{
		std::cout << images[i] << "  -->  "<<colorspace[i] << std::endl;
	}*/
	//PostProcessAsset("D:/test/test2/maya3.usda", "Elements_aks");
	/*for each (auto& image in images)
	{
		std::cout << image.first << "--->" << image.second << std::endl;
	}*/
	for (int i = 0; i < argc; i++)
	{
		std::cout << argv[i];
	}
	std::cin.get();
	return 0;
}