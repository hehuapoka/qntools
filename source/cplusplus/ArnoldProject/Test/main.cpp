#pragma once
#include <ai.h>
#include <cstdio>
#include <vector>

void SetShapeArrayFromVector(const std::vector<AtNode*>& n_v,AtNode* node,const char* name)
{
	AtArray* n_a = AiArrayAllocate(n_v.size(), 1, AI_TYPE_NODE);
	for (size_t i = 0; i < n_v.size(); i++)
	{
		AiArraySetPtr(n_a, i, n_v[i]);
	}
	AiNodeSetArray(node, name, n_a);
}
void GetShapeArrayToVector(std::vector<AtNode*>& n_v,AtNode* node, const char* name)
{
	const AtArray* n_a = AiNodeGetArray(node, name);
	for (size_t i = 0; i < AiArrayGetNumElements(n_a); i++)
	{
		n_v.push_back(static_cast<AtNode*>(AiArrayGetPtr(n_a, i)));
	}
}
int main()
{
	// start an Arnold session, log to both a file and the console
	AiBegin();
	AiMsgSetLogFileName("scene1.log");
	AiMsgSetConsoleFlags(AI_LOG_ALL);

	


	//AtNode* create_sphere = AiNode("create_spheres");
	/*AtArray* a = AiArray(6, 2, AI_TYPE_VECTOR2);
	uint32_t num_a = AiArrayGetNumElements(a);
	uint8_t num_b = AiArrayGetNumKeys(a);
	size_t num_c = AiArrayGetDataSize(a);
	size_t num_d = AiArrayGetKeySize(a);


	char str[80];
	sprintf(str, "%d-->%d-->%d-->%d-->%d", num_a,num_b,num_c,num_d,sizeof(float));
	AiMsgDebug(str);*/

	AtNode* sphere = AiNode("sphere", "sphere0");
	std::vector<AtNode*> a;
	AtNode* light0=AiNode("point_light", "light0");
	AtNode* light1=AiNode("point_light", "light1");
	a.push_back(light0);
	a.push_back(light1);

	//AiNodeSetArray(sphere, "light_group", n_p);
	SetShapeArrayFromVector(a, sphere, "light_group");

	//AiASSWrite("test.ass");
	std::vector<AtNode*> b;
	GetShapeArrayToVector(b, sphere, "light_group");

	for (AtNode* a : b)
	{
		AiMsgDebug(AiNodeGetName(a));
	}



	AiEnd();

	return 0;
}