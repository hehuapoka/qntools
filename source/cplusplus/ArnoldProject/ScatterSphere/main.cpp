#include <ai.h>
#include <sstream>
#include <vector>
AI_OPERATOR_NODE_EXPORT_METHODS(OpMethods);


node_parameters
{
    AiParameterStr("selection_shape", "");
    AiParameterStr("selection_light", "");
    //AiParameterBool("shadow_by_light", true);
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

    //获取灯光
    AtNodeIterator* lightsIt = AiUniverseGetNodeIterator(AI_NODE_LIGHT);

    std::vector<AtNode*> lights;
    while (!AiNodeIteratorFinished(lightsIt))
    {
        AtNode* node_l = AiNodeIteratorGetNext(lightsIt);
        if (node_l)
        {
            lights.push_back(node_l);
        }
    }
    AiNodeIteratorDestroy(lightsIt);




    //循环每一个shape
    AtNodeIterator* shapesIt = AiUniverseGetNodeIterator(AiNodeGetUniverse(op),AI_NODE_SHAPE);
    while (!AiNodeIteratorFinished(shapesIt))
    {
        AtNode* node_s = AiNodeIteratorGetNext(shapesIt);

        if (AiOpMatchNodeSelection(node_s, shape_name, true, op))
        {
            AiNodeSetBool(node_s, AtString("matte"), true);
            //AtArray * n_a =AiNodeGetArray(node_s, "light_group");
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