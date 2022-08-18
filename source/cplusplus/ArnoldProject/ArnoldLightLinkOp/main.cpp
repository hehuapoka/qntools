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
    for (size_t i=0; i<n_v.size(); i++)
    {
        if (!inVector(n_v[i], n_v1)) out_v.push_back(n_v[i]);
    }
    return out_v;
}

node_parameters
{
    AiParameterStr("selection_shape", "");
    AiParameterStr("selection_light", "");

    AiParameterBool("shadow_by_light", true);
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
    AtString shape_name = AiNodeGetStr(op,"selection_shape");
    AtString light_name = AiNodeGetStr(op, "selection_light");
    bool shadow_by_light = AiNodeGetBool(op, "shadow_by_light");

    //获取灯光
    AtNodeIterator* lightsIt = AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_LIGHT);

    std::vector<AtNode*> lights_all;
    std::vector<AtNode*> lights_sel;

    while (!AiNodeIteratorFinished(lightsIt))
    {
        AtNode* node_l = AiNodeIteratorGetNext(lightsIt);
        if (node_l)
        {
            if (AiOpMatchNodeSelection(node_l, light_name, true, op))
            {
                lights_sel.push_back(node_l);
            }  
            lights_all.push_back(node_l);
        }
    }
    AiNodeIteratorDestroy(lightsIt);




    //循环每一个shape
    AtNodeIterator* shapesIt = AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_SHAPE);//AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_SHAPE);
    while (!AiNodeIteratorFinished(shapesIt))
    {
        AtNode* node_s = AiNodeIteratorGetNext(shapesIt);

        std::vector<AtNode*> shape_lights;
        GetShapeArrayToVector(shape_lights, node_s, "light_group");

        if (!AiOpMatchNodeSelection(node_s, shape_name, true, op) && lights_sel.size() > 0)
        {
            if (shape_lights.size() < 1)
            {
                AiNodeSetBool(node_s, "use_light_group", true); //use_shadow_group
                std::vector<AtNode*> sub_v = SubVector(lights_all, lights_sel);
                SetShapeArrayFromVector(sub_v, node_s, "light_group");
                if (shadow_by_light)
                {
                    AiNodeSetBool(node_s, "use_shadow_group", true);
                    SetShapeArrayFromVector(sub_v, node_s, "shadow_group");
                }
                
            }
            else
            {
                //AiNodeSetBool(node_s, AtString("matte"), true);
                std::vector<AtNode*> sub_v = SubVector(shape_lights, lights_sel);
                SetShapeArrayFromVector(sub_v, node_s, "light_group");

                if (shadow_by_light)
                {
                    SetShapeArrayFromVector(sub_v, node_s, "shadow_group");
                }
            }
            /*AiMsgError("lights_shape-->%d", shape_lights.size());
            AiMsgError("lights_all-->%d", lights_all.size());
            AiMsgError("lights_sel-->%d", lights_sel.size());*/
            AiMsgWarning("lights_sel-->%s", AiNodeGetName(node_s));
            //AiNodeSetBool(node_s, AtString("matte"), true);
            //SetShapeArrayFromVector(a, sphere, "light_group");
        }
    }
    AiNodeIteratorDestroy(shapesIt);




    return true;
}

operator_post_cook
{
    return true;
}

node_loader
{
    if (i > 0) return false;

    node->methods = OpMethods;
    node->output_type = AI_TYPE_NONE;
    node->name = AtString("light_link_op");
    node->node_type = AI_NODE_OPERATOR;
    strcpy_s(node->version, AI_VERSION);

    return true;
}