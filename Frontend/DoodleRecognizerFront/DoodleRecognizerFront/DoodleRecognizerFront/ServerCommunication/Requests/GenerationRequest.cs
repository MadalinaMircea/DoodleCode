using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    [Serializable]
    class GenerationRequest
    {
        public GenerationRequest(List<string> classes, string output_File)
        {
            Classes = classes;
            Output_File = output_File;
        }

        public List<string> Classes { get; set; }
        public string Output_File { get; set; }
    }
}
