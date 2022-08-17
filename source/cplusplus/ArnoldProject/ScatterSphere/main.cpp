#include <ai.h>
#include <sstream>
#include <vector>
AI_OPERATOR_NODE_EXPORT_METHODS(OpMethods);


node_parameters
{
    AiParameterStr("selection_shape", "");
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
    //循环每一个shape
    AtNodeIterator* shapesIt = AiUniverseGetNodeIterator(AI_NODE_SHAPE);
    while (!AiNodeIteratorFinished(shapesIt))
    {
        AtNode* node_s = AiNodeIteratorGetNext(shapesIt);

        if (AiOpMatchNodeSelection(node_s, shape_name, true, op))
        {
            AiNodeSetBool(node_s, AtString("matte"), true);
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
    node->name = AtString("scatter_sphere");
    node->node_type = AI_NODE_OPERATOR;
    strcpy_s(node->version, AI_VERSION);

    return true;
}