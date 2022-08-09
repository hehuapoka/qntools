#pragma once
#include "stagetool.h"
#include <vector>
#include <string>
#include <map>
int main()
{
	std::map<std::string, std::string> images;
	//std::vector<std::string> images;
	//std::vector<std::string> colorspace;
	GetAssetTexture("D:/test/test2/maya3.usda",images);
	//std::pair<const std::string, const std::string> i;
	/*for (int i =0 ;i<images.size();i++)
	{
		std::cout << images[i] << "  -->  "<<colorspace[i] << std::endl;
	}*/
	for each (auto& image in images)
	{
		std::cout << image.first << "--->" << image.second << std::endl;
	}
	return 0;
}