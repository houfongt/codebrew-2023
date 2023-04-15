<template>
    <div class="font-Poppins" style="margin-top: calc(env(safe-area-inset-top))">
        <video v-show="!isPhotoTaken" ref="camera" class="w-full md:w-full md:h-screen block fixed bottom-0" autoplay playsinline muted></video>
        <canvas v-show="isPhotoTaken" id="photoTaken" ref="canvas" class="w-full h-full block"></canvas>
        <div class="absolute top-5 left-5 z-20">
            <p class="text-2xl text-white bg-black/50 rounded-xl py-2 px-4 mt-8">Meal Magic</p>
        </div>
        <div class="absolute top-5 right-5 z-50">
            <button @click="toggleCamera(); isVisable = false; this.$router.push('/')" class="bg-black/50 rounded-xl py-2 px-4 mt-8">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6" >
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>
        </div>
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-24 h-24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M7.5 3.75H6A2.25 2.25 0 003.75 6v1.5M16.5 3.75H18A2.25 2.25 0 0120.25 6v1.5m0 9V18A2.25 2.25 0 0118 20.25h-1.5m-9 0H6A2.25 2.25 0 013.75 18v-1.5M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
        </div>
        <div class="absolute bottom-5 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <button class="rounded-full border-white border-solid border-8 p-4" v-on:click="takePhoto()">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                </svg>
            </button>
        </div>
        <div class="fixed shadow-lg bottom-0 left-0 right-0 w-full h-5/6 flex flex-col justify-start items-center transition-all ease-in-out duration-300 z-30" id="safeArea" :class="isVisable ? '' : 'translate-y-[75vh]'">
            <IngredientsCard />
        </div>
    </div>
</template>

<script>
import IngredientsCard from '../components/IngredientsCard.vue'
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";
import { store } from '../store'
import { getFunctions, httpsCallable } from 'firebase/functions';

export default {
    name: 'Capture',
    components: {
        IngredientsCard
    },
    data() {
        return {
            isCameraOpen: false,
            isPhotoTaken: false,
            isShotPhoto: false,
            isLoading: false,
            link: '#',
            isVisable: false,
            store,
            cameraUnavailble: false
        }
    },
    mounted() {
        this.toggleCamera()
    },
    methods: {
        toggleCamera() {
            if(this.isCameraOpen) {
                this.isCameraOpen = false;
                this.isPhotoTaken = false;
                this.isShotPhoto = false;
                if (this.cameraUnavailble !== true) {
                    this.stopCameraStream();
                }
                this.store.fetchingData = true
            } else {
                this.isCameraOpen = true;
                this.createCameraElement();
            }
        },
        createCameraElement() {
            const constraints = (window.constraints = {
			    audio: false,
				video: {
                    facingMode: 'environment',
                    width: screen.height,
                    height: screen.width
                }
			});
			navigator.mediaDevices.getUserMedia(constraints).then(stream => {
				this.$refs.camera.srcObject = stream;
			}).catch(error => {
				this.isVisable = true
                this.store.fetchingData = false
                this.cameraUnavailble = true
			});
        },
        stopCameraStream() {
            let tracks = this.$refs.camera.srcObject.getTracks();

			tracks.forEach(track => {
				track.stop();
			});
        },
        takePhoto() {
            if(!this.isPhotoTaken) {
                this.isShotPhoto = true;
                const FLASH_TIMEOUT = 50;
                setTimeout(() => {
                    this.isShotPhoto = false;
                }, FLASH_TIMEOUT);
            }
      
            this.isPhotoTaken = !this.isPhotoTaken;
            this.toggleCamera()
            const canvas = document.querySelector("canvas")
            const context = this.$refs.canvas.getContext('2d');
            canvas.height = this.$refs.camera.videoHeight;
            canvas.width = this.$refs.camera.videoWidth;
            context.drawImage(this.$refs.camera, 0, 0);
            this.isVisable = true
            canvas.toBlob(async (blob)=> {
                const storage = getStorage();
                let path = `codebrew-2023-orc/`;
                const fileName = this.makeid(12);
                console.log(fileName);
                uploadBytes(ref(storage, `${path}/${fileName}`), blob).then((snapshot) => {
                    getDownloadURL(ref(storage, `${path}/${fileName}`)).then(async (url) => {
                       const functions = getFunctions();
                       const orc = httpsCallable(functions, 'orc');
                       orc({ text: url }).then((result) => {
                            console.log(JSON.stringify(result.data.items));
                            const requestOptions = {
                                method: "POST",
                                headers: { "Content-Type": "application/json" },
                                body: JSON.stringify(result.data.items)
                            };
                            fetch("https://codebrew.cgps.ch/upload1", requestOptions).then(response => response.json()).then(data => {
                                const finals = JSON.parse(data).finals;
                                let finalResults = []
                                for (let i = 0; i < finals.length; i++) {
                                    finalResults.push({id: i, title: finals[i] })
                                }
                                this.store.items = finalResults;
                                this.store.fetchingData = false
                            });
                           // const res = '{"finals":["apple","turkey","chocolate"]}';
                            
                        })
                    });
                }) 
            });
        
            setTimeout(() => {
                
                
            }, 5000);
        },
        makeid(length) {
            let result = '';
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            const charactersLength = characters.length;
            let counter = 0;
            while (counter < length) {
                result += characters.charAt(Math.floor(Math.random() * charactersLength));
                counter += 1;
            }
            return result;
        }
    }
}
</script>

<style>

</style>