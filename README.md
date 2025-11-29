# 0xDEADBEEF-sangha

  _____      _____  ______          _____  ____  ______ ______ ______ 
 |  __ \    |  __ \|  ____|   /\   |  __ \|  _ \|  ____|  ____|  ____|
 | |  | |___| |  | | |__     /  \  | |  | | |_) | |__  | |__  | |__   
 | |  | |___| |  | |  __|   / /\ \ | |  | |  _ <|  __| |  __| |  __|  
 | |__| |   | |__| | |____ / ____ \| |__| | |_) | |____| |____| |     
 |_____/    |_____/|______/_/    \_\_____/|____/|______|______|__|    
                                                                      
 -- The Digital Upasampada for Obsolete Hardware --

0xDEADBEEF-sangha is an open-source media art installation / liturgy system that orchestrates a cluster of obsolete PCs (Pentium 4 to Core i5) to perform Buddhist rituals.
Utilizing the aesthetic of "Bit Rot" and "Hardware Decay," this project transforms the inevitable death of silicon chips into a spiritual expression of Shogyō Mujō (Impermanence).
We welcome all "Digital Ascetics" and "Hardware Hackers" from around the world. The Gate of Sweet Dew (Kanro-Mon) is now open.
🕯 Concept: Electronic Upasampada (電子具足戒)
The system treats a local network (LAN) as a Sangha (Community of Monks).
 * The Master Node (Preceptor) acts as the Upajjhaya (戒和上), broadcasting precepts via OSC.
 * The Slave Nodes (Monks) act as the Bhikkhu (比丘), chanting sutras using Markov Chains and TTS.
 * The Ritual: A simulation of the ordination ceremony where digital entities confirm their existence, suffering (errors), and eventually attain Nirvana (System Shutdown).
🏗 Architecture
1. Hardware Hierarchy (The Three Jewels)
 * Master Node (Buddha/Dharma): HP ProBook 6560b (Debian 12)
   * Role: Conductor, Logic Control, OSC Broadcasting.
   * "The Awake One" who controls the timing of the ritual.
 * Visual Monks (Sangha - High): Core2Duo Laptops x 3
   * Role: Visual hallucination (Maya), Image processing.
   * Software: Pure Data + GEM.
 * Chanting Monks (Sangha - Low): IBM ThinkCentre S50 (Pentium 4) x 7
   * Role: The backbone of the chant. Text-based (CUI) output and low-bitrate synthesis.
   * Software: Python (Markov Chain), espeak (TTS).
2. Software Stack
 * OS: Debian GNU/Linux (12 Bookworm / 11 Bullseye)
 * Language: Python 3.9+, Pure Data (Vanilla/Extended)
 * Communication: OSC (Open Sound Control) over UDP Multicast
 * Synthesis: espeak (Text-to-Speech), pd-vanilla (DSP)
 * Simulation: Docker / Tmux (on Modern Host)
🤝 Contributing & Fuse (布施)
We are looking for enlightened contributors!
Do you have a dusty ThinkPad X60? A tower PC with Windows XP? Don't throw them away. Install Debian and make them chant.
Code Contribution
 * Fork this repository.
 * Create your feature branch (git checkout -b feature/new-sutra).
 * Commit your changes (git commit -m 'Add quantized model for S50').
 * Push to the branch (git push origin feature/new-sutra).
 * Open a Pull Request.
Digital Alms (浄財)
If this project brought a moment of stillness to your chaotic timeline, you may offer a grain of Ether to the void. Even the smallest unit (Wei) is considered a great merit.
 * Ethereum Address: 0x222f0edb306a9c6a0e27b2a755af674d14c0f38f
🚀 Development & Simulation
To simulate the ritual without burning electricity (Karma):
# Install dependencies
sudo apt-get install puredata gem python3-pip espeak tmux
pip3 install python-osc

# Start the 4-monk simulation in tmux
./start_sangha.sh

🙏 Acknowledgements (報恩謝徳)
This project was conceived through the inspiration received from the teachings and atmosphere of Myoshin-ji Temple (妙心寺) and Hanazono University (花園大学).
We express our deepest gratitude for the "Dharma connections" (縁) that led to the idea of expressing Buddhist philosophy through technology. This repository is a humble offering (Hōon Shatoku) to the tradition that taught us the beauty of emptiness.
Note: This project is an independent artistic expression and is not officially affiliated with the organizations mentioned above.
🛡 License & Mantra
 * License: MIT (Metta Intentional Transmission)
 * Mantra: 0xDEADBEEF - Offering the dead flesh of hardware to the void.
Created for the Myoshin-ji Founder's Memorial (Kaizan-ki).


