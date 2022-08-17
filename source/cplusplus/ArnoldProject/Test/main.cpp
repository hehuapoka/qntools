#include <ai.h>

int main()
{
	// start an Arnold session, log to both a file and the console
	AiBegin();
	AiMsgSetLogFileName("scene1.log");
	AiMsgSetConsoleFlags(AI_LOG_ALL);

	// create a sphere geometric primitive
	/*AtNode* sph = AiNode("sphere");
	AiNodeSetStr(sph, "name", "mysphere");
	AiNodeSetVec(sph, "center", 0.0f, 4.0f, 0.0f);
	AiNodeSetFlt(sph, "radius", 4.0f);*/


	AtNode* create_sphere = AiNode("create_spheres");
	/*AiNodeSetStr(sph, "name", "mysphere");
	AiNodeSetVec(sph, "center", 0.0f, 4.0f, 0.0f);
	AiNodeSetFlt(sph, "radius", 4.0f);*/
	


	// create a red standard surface shader
	/*AtNode* shader1 = AiNode("standard_surface");
	AiNodeSetStr(shader1, "name", "myshader1");
	AiNodeSetRGB(shader1, "base_color", 1.0f, 0.02f, 0.02f);
	AiNodeSetFlt(shader1, "specular", 0.05f);*/


	// assign the shaders to the geometric objects
	//AiNodeSetPtr(sph, "shader", shader1);





	// create a perspective camera
	AtNode* camera = AiNode("persp_camera");
	AiNodeSetStr(camera, "name", "mycamera");
	// position the camera (alternatively you can set 'matrix')
	AiNodeSetVec(camera, "position", 0.f, 10.f, 35.f);
	AiNodeSetVec(camera, "look_at", 0.f, 3.f, 0.f);
	AiNodeSetFlt(camera, "fov", 45.f);

	AtNode* light = AiNode("skydome_light");
	AiNodeSetStr(light, "name", "domelight");
	AiNodeSetFlt(light, "intensity", 0.3f); // alternatively, use 'exposure'
	// create a point light source
	AtNode* light1 = AiNode("point_light");
	AiNodeSetStr(light1, "name", "mylight");
	// position the light (alternatively use 'matrix')
	AiNodeSetVec(light1, "position", 15.f, 30.f, 15.f);
	AiNodeSetFlt(light1, "intensity", 4500.f); // alternatively, use 'exposure'
	AiNodeSetFlt(light1, "radius", 4.f); // for soft shadows

	// get the global options node and set some options
	AtNode* options = AiUniverseGetOptions();
	AiNodeSetInt(options, "AA_samples", 8);
	AiNodeSetInt(options, "xres", 480);
	AiNodeSetInt(options, "yres", 360);
	AiNodeSetInt(options, "GI_diffuse_depth", 4);
	// set the active camera (optional, since there is only one camera)
	AiNodeSetPtr(options, "camera", camera);
	AiNodeSetPtr(options, "operator", create_sphere);

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

	
	//save ass
	//AiASSWrite("scene.ass");
	// finally, render the image!
	AiRender(AI_RENDER_MODE_CAMERA);

	// ... or you can write out an .ass file instead
	//AiASSWrite("scene1.ass", AI_NODE_ALL, FALSE);

	// Arnold session shutdown
	AiEnd();

	return 0;
}