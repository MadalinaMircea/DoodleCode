using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    class DetectionJsonResponse :JsonResponse
    {
        public DetectionResponse Response { get; set; }
    }
}
