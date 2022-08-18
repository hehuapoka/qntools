#include <ai.h>
#include <sstream>
#include <vector>
AI_OPERATOR_NODE_EXPORT_METHODS(OpMethods);


node_parameters
{
    AiParameterStr("selection", "");
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


    //循环每一个shape
    /*AtNodeIterator* shapesIt = AiUniverseGetNodeIterator(AI_NODE_SHAPE);
    while (!AiNodeIteratorFinished(shapesIt))
    {
        AtNode* node_s = AiNodeIteratorGetNext(shapesIt);



    }
    AiNodeIteratorDestroy(shapesIt);*/

    const AtNodeEntry* a = AiNodeGetNodeEntry(node);
    if (AiNodeEntryGetType(a) != AI_NODE_SHAPE) return 1;

    AiMsgWarning("info----->%s", AiNodeGetName(node));




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
    node->name = AtString("make_info");
    node->node_type = AI_NODE_OPERATOR;
    strcpy_s(node->version, AI_VERSION);

    return true;
}