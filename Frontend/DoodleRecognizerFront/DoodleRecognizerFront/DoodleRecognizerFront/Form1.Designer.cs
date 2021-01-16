
namespace DoodleRecognizerFront
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.ImagePictureBox = new System.Windows.Forms.PictureBox();
            this.LoadButton = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.RotateButton = new System.Windows.Forms.Button();
            this.DetectedPanel = new System.Windows.Forms.Panel();
            this.GenerateCodeButton = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.DetectedBoxList = new System.Windows.Forms.CheckedListBox();
            this.MainPanel = new System.Windows.Forms.Panel();
            this.button2 = new System.Windows.Forms.Button();
            this.FirstPanel = new System.Windows.Forms.Panel();
            this.SpeechChoiceButton = new System.Windows.Forms.Button();
            this.ImagesChoiceButton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.SpeechPanel = new System.Windows.Forms.Panel();
            this.SpokenListBox = new System.Windows.Forms.ListBox();
            this.SpeechGenerateButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.RecordingButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).BeginInit();
            this.DetectedPanel.SuspendLayout();
            this.MainPanel.SuspendLayout();
            this.FirstPanel.SuspendLayout();
            this.SpeechPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // ImagePictureBox
            // 
            this.ImagePictureBox.BackColor = System.Drawing.Color.MintCream;
            this.ImagePictureBox.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.ImagePictureBox.Location = new System.Drawing.Point(17, 60);
            this.ImagePictureBox.Name = "ImagePictureBox";
            this.ImagePictureBox.Size = new System.Drawing.Size(930, 534);
            this.ImagePictureBox.TabIndex = 0;
            this.ImagePictureBox.TabStop = false;
            // 
            // LoadButton
            // 
            this.LoadButton.BackColor = System.Drawing.Color.Turquoise;
            this.LoadButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoadButton.Location = new System.Drawing.Point(368, 600);
            this.LoadButton.Name = "LoadButton";
            this.LoadButton.Size = new System.Drawing.Size(194, 54);
            this.LoadButton.TabIndex = 1;
            this.LoadButton.Text = "Load Picture";
            this.LoadButton.UseVisualStyleBackColor = false;
            this.LoadButton.Click += new System.EventHandler(this.button1_Click);
            this.LoadButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(275, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(287, 32);
            this.label1.TabIndex = 4;
            this.label1.Text = "Choose your picture";
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // RotateButton
            // 
            this.RotateButton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("RotateButton.BackgroundImage")));
            this.RotateButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.RotateButton.Enabled = false;
            this.RotateButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RotateButton.Location = new System.Drawing.Point(568, 600);
            this.RotateButton.Name = "RotateButton";
            this.RotateButton.Size = new System.Drawing.Size(60, 54);
            this.RotateButton.TabIndex = 8;
            this.RotateButton.UseVisualStyleBackColor = true;
            this.RotateButton.Click += new System.EventHandler(this.button3_Click);
            // 
            // DetectedPanel
            // 
            this.DetectedPanel.Controls.Add(this.GenerateCodeButton);
            this.DetectedPanel.Controls.Add(this.label4);
            this.DetectedPanel.Controls.Add(this.DetectedBoxList);
            this.DetectedPanel.Location = new System.Drawing.Point(0, 0);
            this.DetectedPanel.Name = "DetectedPanel";
            this.DetectedPanel.Size = new System.Drawing.Size(1187, 687);
            this.DetectedPanel.TabIndex = 14;
            // 
            // GenerateCodeButton
            // 
            this.GenerateCodeButton.BackColor = System.Drawing.Color.Turquoise;
            this.GenerateCodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GenerateCodeButton.Location = new System.Drawing.Point(941, 263);
            this.GenerateCodeButton.Name = "GenerateCodeButton";
            this.GenerateCodeButton.Size = new System.Drawing.Size(222, 133);
            this.GenerateCodeButton.TabIndex = 2;
            this.GenerateCodeButton.Text = "Generate my code!";
            this.GenerateCodeButton.UseVisualStyleBackColor = false;
            this.GenerateCodeButton.Click += new System.EventHandler(this.GenerateCodeButton_Click);
            this.GenerateCodeButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(133, 25);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(495, 32);
            this.label4.TabIndex = 1;
            this.label4.Text = "What objects are of interest to you?";
            // 
            // DetectedBoxList
            // 
            this.DetectedBoxList.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DetectedBoxList.FormattingEnabled = true;
            this.DetectedBoxList.Location = new System.Drawing.Point(17, 79);
            this.DetectedBoxList.Name = "DetectedBoxList";
            this.DetectedBoxList.Size = new System.Drawing.Size(889, 598);
            this.DetectedBoxList.TabIndex = 0;
            this.DetectedBoxList.SelectedIndexChanged += new System.EventHandler(this.DetectedBoxList_SelectedIndexChanged);
            // 
            // MainPanel
            // 
            this.MainPanel.Controls.Add(this.button2);
            this.MainPanel.Controls.Add(this.RotateButton);
            this.MainPanel.Controls.Add(this.label1);
            this.MainPanel.Controls.Add(this.ImagePictureBox);
            this.MainPanel.Controls.Add(this.LoadButton);
            this.MainPanel.Location = new System.Drawing.Point(0, 0);
            this.MainPanel.Name = "MainPanel";
            this.MainPanel.Size = new System.Drawing.Size(1214, 684);
            this.MainPanel.TabIndex = 3;
            // 
            // button2
            // 
            this.button2.BackColor = System.Drawing.Color.Turquoise;
            this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(962, 334);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(201, 95);
            this.button2.TabIndex = 9;
            this.button2.Text = "This is my image!";
            this.button2.UseVisualStyleBackColor = false;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            this.button2.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // FirstPanel
            // 
            this.FirstPanel.Controls.Add(this.SpeechChoiceButton);
            this.FirstPanel.Controls.Add(this.ImagesChoiceButton);
            this.FirstPanel.Controls.Add(this.label2);
            this.FirstPanel.Location = new System.Drawing.Point(0, 0);
            this.FirstPanel.Name = "FirstPanel";
            this.FirstPanel.Size = new System.Drawing.Size(1187, 687);
            this.FirstPanel.TabIndex = 15;
            // 
            // SpeechChoiceButton
            // 
            this.SpeechChoiceButton.BackColor = System.Drawing.Color.Turquoise;
            this.SpeechChoiceButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SpeechChoiceButton.Location = new System.Drawing.Point(725, 247);
            this.SpeechChoiceButton.Name = "SpeechChoiceButton";
            this.SpeechChoiceButton.Size = new System.Drawing.Size(307, 164);
            this.SpeechChoiceButton.TabIndex = 3;
            this.SpeechChoiceButton.Text = "Generate code from spoken words";
            this.SpeechChoiceButton.UseVisualStyleBackColor = false;
            this.SpeechChoiceButton.Click += new System.EventHandler(this.SpeechChoiceButton_Click);
            this.SpeechChoiceButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // ImagesChoiceButton
            // 
            this.ImagesChoiceButton.BackColor = System.Drawing.Color.Turquoise;
            this.ImagesChoiceButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ImagesChoiceButton.Location = new System.Drawing.Point(130, 247);
            this.ImagesChoiceButton.Name = "ImagesChoiceButton";
            this.ImagesChoiceButton.Size = new System.Drawing.Size(307, 164);
            this.ImagesChoiceButton.TabIndex = 2;
            this.ImagesChoiceButton.Text = "Generate code from images";
            this.ImagesChoiceButton.UseVisualStyleBackColor = false;
            this.ImagesChoiceButton.Click += new System.EventHandler(this.ImagesChoiceButton_Click);
            this.ImagesChoiceButton.MouseEnter += new System.EventHandler(this.Button_MouseEnter);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(389, 79);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(444, 32);
            this.label2.TabIndex = 1;
            this.label2.Text = "How would you like to proceed?";
            // 
            // SpeechPanel
            // 
            this.SpeechPanel.BackColor = System.Drawing.Color.PeachPuff;
            this.SpeechPanel.Controls.Add(this.RecordingButton);
            this.SpeechPanel.Controls.Add(this.SpokenListBox);
            this.SpeechPanel.Controls.Add(this.SpeechGenerateButton);
            this.SpeechPanel.Controls.Add(this.label3);
            this.SpeechPanel.Location = new System.Drawing.Point(0, 0);
            this.SpeechPanel.Name = "SpeechPanel";
            this.SpeechPanel.Size = new System.Drawing.Size(1208, 700);
            this.SpeechPanel.TabIndex = 13;
            // 
            // SpokenListBox
            // 
            this.SpokenListBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SpokenListBox.FormattingEnabled = true;
            this.SpokenListBox.ItemHeight = 31;
            this.SpokenListBox.Location = new System.Drawing.Point(395, 92);
            this.SpokenListBox.Name = "SpokenListBox";
            this.SpokenListBox.Size = new System.Drawing.Size(407, 562);
            this.SpokenListBox.TabIndex = 12;
            // 
            // SpeechGenerateButton
            // 
            this.SpeechGenerateButton.BackColor = System.Drawing.Color.Coral;
            this.SpeechGenerateButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SpeechGenerateButton.Location = new System.Drawing.Point(843, 290);
            this.SpeechGenerateButton.Name = "SpeechGenerateButton";
            this.SpeechGenerateButton.Size = new System.Drawing.Size(288, 148);
            this.SpeechGenerateButton.TabIndex = 9;
            this.SpeechGenerateButton.Text = "Generate my code!";
            this.SpeechGenerateButton.UseVisualStyleBackColor = false;
            this.SpeechGenerateButton.Click += new System.EventHandler(this.SpeechGenerateButton_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(406, 41);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(365, 32);
            this.label3.TabIndex = 4;
            this.label3.Text = "Press the button to record";
            // 
            // RecordingButton
            // 
            this.RecordingButton.BackColor = System.Drawing.Color.Coral;
            this.RecordingButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RecordingButton.Location = new System.Drawing.Point(44, 290);
            this.RecordingButton.Name = "RecordingButton";
            this.RecordingButton.Size = new System.Drawing.Size(310, 148);
            this.RecordingButton.TabIndex = 13;
            this.RecordingButton.Text = "Start Recording";
            this.RecordingButton.UseVisualStyleBackColor = false;
            this.RecordingButton.Click += new System.EventHandler(this.RecordingButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.PaleTurquoise;
            this.ClientSize = new System.Drawing.Size(1208, 699);
            this.Controls.Add(this.SpeechPanel);
            this.Controls.Add(this.MainPanel);
            this.Controls.Add(this.FirstPanel);
            this.Controls.Add(this.DetectedPanel);
            this.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.Name = "Form1";
            this.Text = "Generate Code With Images!";
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).EndInit();
            this.DetectedPanel.ResumeLayout(false);
            this.DetectedPanel.PerformLayout();
            this.MainPanel.ResumeLayout(false);
            this.MainPanel.PerformLayout();
            this.FirstPanel.ResumeLayout(false);
            this.FirstPanel.PerformLayout();
            this.SpeechPanel.ResumeLayout(false);
            this.SpeechPanel.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox ImagePictureBox;
        private System.Windows.Forms.Button LoadButton;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button RotateButton;
        private System.Windows.Forms.Panel DetectedPanel;
        private System.Windows.Forms.Button GenerateCodeButton;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.CheckedListBox DetectedBoxList;
        private System.Windows.Forms.Panel MainPanel;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Panel FirstPanel;
        private System.Windows.Forms.Button SpeechChoiceButton;
        private System.Windows.Forms.Button ImagesChoiceButton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Panel SpeechPanel;
        private System.Windows.Forms.ListBox SpokenListBox;
        private System.Windows.Forms.Button SpeechGenerateButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button RecordingButton;
    }
}

