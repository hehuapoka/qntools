#pragma once
#include <ai.h>
#include <cstdio>
#include <vector>


void Render(AtNode* options)
{
	// create a perspective camera
	AtNode* camera = AiNode("persp_camera");
	AiNodeSetStr(camera, "name", "mycamera");
	// position the camera (alternatively you can set 'matrix')
	AiNodeSetVec(camera, "position", 0.f, 10.f, 35.f);
	AiNodeSetVec(camera, "look_at", 0.f, 3.f, 0.f);
	AiNodeSetFlt(camera, "fov", 45.f);

	// get the global options node and set some options
	AiNodeSetInt(options, "AA_samples", 8);
	AiNodeSetInt(options, "xres", 480);
	AiNodeSetInt(options, "yres", 360);
	AiNodeSetInt(options, "GI_diffuse_depth", 4);
	AiNodeSetPtr(options, "camera", camera);

	// create an output driver node
	AtNode* driver = AiNode("driver_jpeg");
	AiNodeSetStr(driver, "name", "mydriver");
	AiNodeSetStr(driver, "filename", "scene1.jpg");

	// create a gaussian filter node
	AtNode* filter = AiNode("gaussian_filter");
	AiNodeSetStr(filter, "name", "myfilter");

	// assign the driver and filter to the main (beauty) AOV,
	// which is called "RGBA" and is of type RGBA
	AtArray* outputs_array = AiArrayAllocate(1, 1, AI_TYPE_STRING);
	AiArraySetStr(outputs_array, 0, "RGBA RGBA myfilter mydriver");
	AiNodeSetArray(options, "outputs", outputs_array);

	// finally, render the image!
	AiRender(AI_RENDER_MODE_CAMERA);
}
int main()
{
	// start an Arnold session, log to both a file and the console
	AiBegin();
	AiMsgSetLogFileName("scene1.log");
	AiMsgSetConsoleFlags(AI_LOG_ALL);

	AiASSLoad("E:/Work/test/maya/a.ass");

	AtNode* sphere = AiNode("sphere", "sphere0");
	AtNode* light0=AiNode("point_light", "light0");
	AtNode* light1=AiNode("point_light", "light1");



	AtNode* u = AiNodeLookUpByName("/Chars_xiaogui_1/Chars_xiaogui_1Shape");
	/*if (u)
	{
		void* u_data=AiNodeGetPluginData(u);


		AiMsgDebug("--->%s-->", AiNodeGetName(u), procedural_num_nodes(u,u_data));
	}*/
	/*AiNodeGetPluginData()
	AtProcNumNodes();
	AtProcGetNode();*/







	AtNode* make_info = AiNode("make_info", "makeinfos");
	AtNode* options = AiUniverseGetOptions();
	AiNodeSetPtr(options, "operator", static_cast<void*>(make_info));


	

	//AiMsgDebug("--->%d",AiNodeIs(make_info,AtString("make_info")));
	Render(options);
	AiEnd();

	return 0;
}