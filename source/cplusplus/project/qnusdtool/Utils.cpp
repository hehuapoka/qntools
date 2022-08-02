#include "Utils.h"

void showVector(const std::vector<std::string>& old_paths)
{
    for (auto i : old_paths)
    {
        std::cout << i << std::endl;
    }
}

std::string GetRelPath(std::string path, const std::string& layer_path)
{

    //boost::filesystem::path(layer_path).parent_path()
    std::string new_path = static_cast<char>(tolower(path[0])) + path.substr(1, path.size() - 1);
    std::string new_path_old = static_cast<char>(tolower(layer_path[0])) + layer_path.substr(1, layer_path.size() - 1);

    std::string solver_path = boost::filesystem::relative(new_path, boost::filesystem::path(new_path_old).parent_path()).string();
    if (solver_path.empty()) return path;
    boost::replace_all(solver_path, "\\", "/");

    return solver_path;
}