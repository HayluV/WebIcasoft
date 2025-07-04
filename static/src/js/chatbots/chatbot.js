 // WhatsApp
        const whatsappButton = document.getElementById('whatsappButton');
        const whatsappModal = document.getElementById('whatsappModal');
        const closeModal = document.getElementById('closeModal');
        
        whatsappButton.addEventListener('click', () => {
            whatsappModal.classList.add('active');
        });
        
        closeModal.addEventListener('click', () => {
            whatsappModal.classList.remove('active');
        });
        
        // Chatbot Robot
        const robotLauncher = document.getElementById('robotLauncher');
        const robotInterface = document.getElementById('robotInterface');
        const closeRobot = document.getElementById('closeRobot');
        const robotInput = document.getElementById('robotInput');
        const sendRobotMessage = document.getElementById('sendRobotMessage');
        const robotBody = document.getElementById('robotBody');
        
        let isRobotOpen = false;
        
        robotLauncher.addEventListener('click', () => {
            isRobotOpen = !isRobotOpen;
            robotInterface.classList.toggle('active', isRobotOpen);
            if (isRobotOpen) robotInput.focus();
        });
        
        closeRobot.addEventListener('click', () => {
            isRobotOpen = false;
            robotInterface.classList.remove('active');
        });
        
        function sendMessage() {
            const message = robotInput.value.trim();
            if (message) {
                // Mensaje del usuario
                const userMessage = document.createElement('div');
                userMessage.className = 'robot-message';
                userMessage.style.marginLeft = 'auto';
                userMessage.style.backgroundColor = '#e3f2fd';
                userMessage.style.border = '1px solid #bbdefb';
                userMessage.innerHTML = `<p>${message}</p>`;
                robotBody.appendChild(userMessage);
                
                robotInput.value = '';
                robotBody.scrollTop = robotBody.scrollHeight;
                
                // Respuesta del robot (simulada)
                setTimeout(() => {
                    const responses = [
                        "¡Interesante pregunta! Déjame procesarla...",
                        "Como asistente robótico, recomendaría consultar nuestra sección de ayuda.",
                        "🤖 *Bip bop* Estoy analizando tu solicitud...",
                        "Puedo ayudarte con eso. ¿Necesitas más detalles?",
                        "¡Vaya! Buena pregunta. ¿Quieres que te guíe paso a paso?"
                    ];
                    const randomResponse = responses[Math.floor(Math.random() * responses.length)];
                    
                    const botMessage = document.createElement('div');
                    botMessage.className = 'robot-message';
                    botMessage.innerHTML = `<p>${randomResponse}</p>`;
                    robotBody.appendChild(botMessage);
                    robotBody.scrollTop = robotBody.scrollHeight;
                }, 1000);
            }
        }
        
        sendRobotMessage.addEventListener('click', sendMessage);
        robotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
        
        // Cerrar modales al hacer clic fuera (en móviles)
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                if (!whatsappModal.contains(e.target) && e.target !== whatsappButton) {
                    whatsappModal.classList.remove('active');
                }
                if (!robotInterface.contains(e.target) && e.target !== robotLauncher) {
                    isRobotOpen = false;
                    robotInterface.classList.remove('active');
                }
            }
        });