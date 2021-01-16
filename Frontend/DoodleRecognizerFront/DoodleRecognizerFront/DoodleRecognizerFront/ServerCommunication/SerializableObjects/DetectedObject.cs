using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoodleRecognizerFront
{
    [Serializable]
    class DetectedObject
    {
        public string Name { get; set; }
        public List<string> Children { get; set; }

        public DetectedObject(string name)
        {
            Name = name;
        }

        public DetectedObject(string name, List<string> children)
        {
            Name = name;
            Children = children;
        }
    }
}
