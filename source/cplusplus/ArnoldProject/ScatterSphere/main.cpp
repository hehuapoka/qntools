#include <ai.h>
#include <sstream>
#include <vector>
AI_OPERATOR_NODE_EXPORT_METHODS(OpMethods);


void SetShapeArrayFromVector(const std::vector<AtNode*>& n_v, AtNode* node, const char* name)
{
    if (n_v.size() < 1) return;
    AtArray* n_a = AiArrayAllocate(n_v.size(), 1, AI_TYPE_NODE);
    for (size_t i = 0; i < n_v.size(); i++)
    {
        AiArraySetPtr(n_a, i, n_v[i]);
    }
    //AiMsgError("size-->%d", AiArrayGetNumElements(n_a));
    /*AtArray* n_orign = AiNodeGetArray(node, name);
    AiArrayResize(n_orign, n_v.size()+1, 1);*/

    AiNodeSetArray(node, name, n_a);
    //AiArrayDestroy(n_a);
}

void GetShapeArrayToVector(std::vector<AtNode*>& n_v, AtNode* node, const char* name)
{
    const AtArray* n_a = AiNodeGetArray(node, name);
    if (AiArrayGetNumElements(n_a) < 1) return;
    for (size_t i = 0; i < AiArrayGetNumElements(n_a); i++)
    {
        n_v.push_back(static_cast<AtNode*>(AiArrayGetPtr(n_a, i)));
    }
}

bool inVector(AtNode* node, const std::vector<AtNode*>& n_v1)
{
    for (size_t i = 0; i < n_v1.size(); i++)
    {
        if (node == n_v1[i])
        {
            return true;
        }
    }
    return false;
}
std::vector<AtNode*> SubVector(const std::vector<AtNode*>& n_v, const std::vector<AtNode*>& n_v1)
{
    std::vector<AtNode*> out_v;
    for (size_t i = 0; i < n_v.size(); i++)
    {
        if (!inVector(n_v[i], n_v1)) out_v.push_back(n_v[i]);
    }
    return out_v;
}

node_parameters
{
    AiParameterStr("selection_shape", "/*");
}

operator_init
{
    return true;
}

operator_cleanup
{
    return true;
}

operator_cook
{
    return true;
}

operator_post_cook
{


    AtString shape_name = AiNodeGetStr(op,"selection_shape");
    //循环每一个shape
    AtNodeIterator* shapesIt = AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_SHAPE);//AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_SHAPE);
    while (!AiNodeIteratorFinished(shapesIt))
    {
        AtNode* node_s = AiNodeIteratorGetNext(shapesIt);

        if (AiOpMatchNodeSelection(node_s, shape_name, true, op))
        {
            AiNodeSetBool(node_s, "matte", true);
        }
        AtNode* parent_node = AiNodeGetParent(node_s);
        AiMsgWarning("lights_sel-->%s-->%s---->%d----->parent: %d",shape_name.c_str(), AiNodeGetName(node_s), AiNodeGetBool(node_s, "matte"), parent_node==NULL);
        
    }
    AiNodeIteratorDestroy(shapesIt);

    return true;
}

node_loader
{
    if (i > 0) return false;

    node->methods = OpMethods;
    node->output_type = AI_TYPE_NONE;
    node->name = AtString("make_info");
    node->node_type = AI_NODE_OPERATOR;
    strcpy_s(node->version, AI_VERSION);

    return true;
}