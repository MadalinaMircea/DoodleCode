using Newtonsoft.Json;
using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront.ServerCommunication
{
    class ServerCommunicator
    {
        public ServerCommunicator()
        {
            
        }

        public string PostRequestDetection(byte[] bytes, out List<string> detected)
        {
            detected = new List<string>();

            try
            {
                string bytesString = Convert.ToBase64String(bytes);

                var client = new RestClient("http://localhost:5000/get_objects");
                client.Timeout = -1;
                var request = new RestRequest(Method.POST);
                request.AddHeader("Content-Type", "application/json");
                string json = "{\"image_bytes\":\"" +
                    bytesString + "\"}";
                request.AddParameter("application/json",
                    json, ParameterType.RequestBody);
                IRestResponse response = client.Execute(request);


                DetectionJsonResponse json_response = JsonConvert.DeserializeObject<DetectionJsonResponse>(response.Content);

                detected = json_response.Response.Detected;
            }
            catch (Exception ex)
            {
                return "There was an error. Sorry! " + ex.Message;
            }

            return "";
        }

        public string PostRequestGeneration(List<string> detected)
        {
            var client = new RestClient("http://localhost:5000/generate_code");
            client.Timeout = -1;
            var request = new RestRequest(Method.POST);
            request.AddHeader("Content-Type", "application/json");


            GenerationRequest gen_req = new GenerationRequest(detected, "Client_Output");
            string json = JsonConvert.SerializeObject(gen_req);
            request.AddParameter("application/json",
                json.ToLower(), ParameterType.RequestBody);
            IRestResponse response = client.Execute(request);

            try
            {
                JsonResponse json_response = JsonConvert.DeserializeObject<JsonResponse>(response.Content);

                return json_response.Code.ToString() + " " + json_response.Error;
            }
            catch (Exception ex)
            {
                return "There was an error. Sorry! " + ex.Message;
            }
        }

        public string PostRequestChildren(List<string> detected)
        {
            var client = new RestClient("http://localhost:5000/generate_code");
            client.Timeout = -1;
            var request = new RestRequest(Method.POST);
            request.AddHeader("Content-Type", "application/json");


            GenerationRequest gen_req = new GenerationRequest(detected, "Client_Output");
            string json = JsonConvert.SerializeObject(gen_req);
            request.AddParameter("application/json",
                json.ToLower(), ParameterType.RequestBody);
            IRestResponse response = client.Execute(request);

            try
            {
                JsonResponse json_response = JsonConvert.DeserializeObject<JsonResponse>(response.Content);

                return json_response.Code.ToString() + " " + json_response.Error;
            }
            catch (Exception ex)
            {
                return "There was an error. Sorry! " + ex.Message;
            }
        }

    }
}
