<template>
    <div class="bg-slate-100 w-full h-screen">
        <div class="flex flex-row gap-0.5 absolute left-0 right-0 w-fit translate-y-1/2 mx-auto bg-slate-200 rounded-md drop-shadow-md overflow-hidden">
            <form @submit.prevent="signupHandler" class="flex flex-col gap-2 justify-center py-2 px-4">
                <h2 class="text-3xl font-semibold mt-2">Sign Up</h2>
                <div class="flex flex-row gap-2">
                    <div class="flex flex-col gap-1.5 mt-1">
                        <label for="first_name">First Name</label>
                        <input v-model="userCredential.first_name" class="outline-none rounded-md p-1" type="text"/>
                    </div>
                    <div class="flex flex-col gap-1.5 mt-1">
                        <label for="last_name">Last Name</label>
                        <input v-model="userCredential.last_name" class="outline-none rounded-md p-1" type="text"/>
                    </div>
                </div>
                <div class="flex flex-col gap-1.5 mt-0.5">
                    <label for="email">Email</label>
                    <input v-model="userCredential.email" class="outline-none rounded-md p-1" type="email"/>
                </div>
                <div class="flex flex-col gap-1.5 mt-0.5">
                    <label for="password">Password</label>
                    <input v-model="userCredential.password" class="outline-none rounded-md p-1" type="password"/>
                </div>
                <div class="flex justify-center items-end gap-2 my-2">
                    <button class="bg-slate-100 hover:bg-slate-300 w-fit p-1.5 rounded-md drop-shadow-md font-medium">Register</button>
                    <p class="text-smnd mb-1">Already have an account? <RouterLink class="text-blue-600 font-medium" :to="{name:'signin'}">Sign In</RouterLink></p>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
    export default {
        data(){
            return {
                userCredential:{
                    first_name:'',
                    last_name:'',
                    email:'',
                    password:''
                }
            }
        },
        methods:{
            signupHandler(){
                let first_name=this.userCredential.first_name.trim()
                let last_name=this.userCredential.last_name.trim()
                let email=this.userCredential.email.trim()
                let password=this.userCredential.password.trim()
                if(first_name&&last_name&&email&&password){
                    this.$store.dispatch('signupUser',{first_name,last_name,email,password})
                }
            }
        }
    }
</script>
