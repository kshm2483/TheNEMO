<template>
    <div class="profile">
        <div class="profile-edit">
            <ul class="profile-edit__list">
                <div id="passwordChange" class="change">
                    <p>비밀번호 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 1" v-if="editToggle != 1">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 1">Close</div>
                </div>
                
                <div v-if="editToggle === 1" class="expand">
                    <ul>
                        <label>
                            <p>이전 비밀번호</p>
                            <input type="password" class="LoginForm__Input"  id="OLDPASSWORD" v-model="oldpassword" placeholder="이전 비밀번호" autocomplete="new-password">
                        </label>

                        <label>
                            <p>새 비밀번호</p>
                            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPassword()}" id="PASSWORD" v-model="password" placeholder="비밀번호" autocomplete="new-password">
                            <p class="checkText" v-if="checkPassword()" >비밀번호는 최소 8글자 이상이어야 합니다.</p>
                        </label>

                        <label>
                            <p>새 비밀번호 확인</p>
                            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPasswordConfirm()}" id="PASSWORDCONFIRM" v-model="passwordconfirm" placeholder="비밀번호 확인" autocomplete="new-password">
                            <p class="checkText" v-if="checkPasswordConfirm()" >비밀번호가 일치하지 않습니다.</p>
                        </label>
                    </ul> 
                </div>
                <div v-if="editToggle === 1" class="btn btn--primary btn--sm" :class="{'btn--disabled' : checkPasswordClear() }">변경하기</div>

                <div id="imgChange" class="change">
                    
                    <p>프로필 이미지 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 2" v-if="editToggle != 2">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 2">Close</div>
                </div>
                <div v-if="editToggle === 2" class="expand">
                    <div class="expand__img">
                        <img :src="userImg" alt="" style="width: 11vw; height: 10vw;">
                        <div  class="file-select">
                            <label>
                                <!-- We can't use a normal button element here, as it would become the target of the label. -->
                                <span class="btn btn--primary">Select File</span>
                                <!-- Now, the file input that we hide. -->
                                <input type="file" @change="changeImg"/>
                            </label>
                            <p v-if="userChangeImg">Selected File: {{userChangeImg}}</p>
                        </div>
                    </div>
                    
                </div>

                <div id="detailChange" class="change">
                    <p>개인 정보 변경</p>
                    <div class="btn btn--sm" @click="editToggle = 3" v-if="editToggle != 3">Expand</div>
                    <div class="btn btn--sm" @click="editToggle = 0" v-if="editToggle === 3">Close</div>
                </div>
                <div v-if="editToggle === 3" class="expand">
                    <ul>
                        <div v-for="items in SignupList" :key="items.label">
                            <p class="label" :id="items.label">{{items.label}}</p>
                            
                            <select :name="items.name" class="LoginForm__Drop" v-model="items.name">
                                <option :value="item.value" v-for="item in items.option" :key="item.value">{{item.text}}</option>
                            </select>
                        </div>
                        <label>
                            <p>한 줄 코멘트</p>
                            <input type="text" style="width:50%; min-width:480px;" :class="{LoginForm__Err : checkUserDescription()}" class="LoginForm__Input" id="USERDESCRIPTION" v-model="userDescription" placeholder="한줄 코멘트">
                            <p class="checkText" v-if="checkUserDescription()" >한 줄 코멘트는 40자를 넘을 수 없습니다.</p>
                        </label>
                        <br>
                    </ul>
                </div>
                <div v-if="editToggle === 3" class="btn btn--primary btn--sm" :class="{'btn--disabled' : checkDetailChangeClear() }" @click="patchData()">저장</div> 
            </ul>
        </div>
        <div class="btn btn--primary btn--lg" @click="Go()">back</div>
    </div>
</template>
<script>
import api from '@/api'
import swal from 'sweetalert';

export default {
    data() {
        return{
            oldpassword: '',
            password : '',
            passwordconfirm : '',
            userDescription: '',

            userImg : require('@/assets/image/defaultUserImage.jpg'),
            userChangeImg : '',

            editToggle : 0,
            editList : [
                {name: '비밀번호 변경', value: 1},
                {name: '프로필 이미지 변경', value: 2},
                {name: '개인 정보 변경', value: 3},
            ],
            SignupList : [
                { label : 'age',
                name : '',
                option: [
                    {text:  "Under 18", value : 1},
                    {text:  "18-24", value : 18},
                    {text:  "25-34", value : 25},
                    {text:  "35-44", value : 35},
                    {text:  "45-49", value : 45},
                    {text:  "50-55", value : 50},
                    {text:  "56+", value : 56},
                ]},
                { label : 'occupation',
                name : '',
                option: [
                    {text:  "other", value : "other"},
                    {text:  "academic/educator", value : "academic/educator"},
                    {text:  "artist", value : "artist"},
                    {text:  "clerical/admin", value : "clerical/admin"},
                    {text:  "college/grad student", value : "college/grad student"},
                    {text:  "customer service", value : "customer service"},
                    {text:  "doctor/health care", value : "doctor/health care"},
                    {text:  "executive/managerial", value : "executive/managerial"},
                    {text:  "farmer", value : "farmer"},
                    {text:  "homemaker", value : "homemaker"},
                    {text:  "K-12 student", value : "K-12 student"},
                    {text:  "lawyer", value : "lawyer"},
                    {text:  "programmer", value : "programmer"},
                    {text:  "retired", value : "retired"},
                    {text:  "sales/marketing", value : "sales/marketing"},
                    {text:  "scientist", value : "scientist"},
                    {text:  "self-employed", value : "self-employed"},
                    {text:  "technician/engineer", value : "technician/engineer"},
                    {text:  "tradesman/craftsman", value : "tradesman/craftsman"},
                    {text:  "unemployed", value : "unemployed"},
                    {text:  "writer", value : "writer"},
                ]},
            ]
        }
    },
    methods: {
        Go() {
            this.$emit('transForm');
            window.scrollTo(0, 0);
        },
        checkPasswordClear() {
        if (this.oldpassword === ''|| this.password === '' || this.passwordconfirm === '' || this.checkPassword() || this.checkPasswordConfirm()) {
            return true
            }
        },
        checkDetailChangeClear() {
        if (this.SignupList[0].name === '' || this.SignupList[1].name === '' || this.checkUserDescription() || this.userDescription === "") {
            return true
            }
        },
        checkPassword() {
            if (this.password != '' && this.password.length <= 7) {
                return true
            }
        },
        checkPasswordConfirm() {
            if (this.passwordconfirm != '' && this.passwordconfirm != this.password) {
                return true
            }
        },
        checkUserDescription() {
            if (this.userDescription != '' && this.userDescription.length > 40) {
                return true
            }
        },
        changeImg(e) {
            console.log(e)
            this.userChangeImg = e.target.files[0].name
        },
        async patchData() {
            const data = JSON.parse(sessionStorage.getItem("drf"))
            const form = { 
                "id" : data.id,
                "age" : this.SignupList[0].name,
                "occupation" : this.SignupList[1].name,
                "description" : this.userDescription
                }
            const result = await api.patchProfileData(form)
            if (result.status === 200) {
                swal({
                    title : "개인 정보 수정을 완료 하였습니다.",
                    text : "이 창은 잠시 후 종료 됩니다.",
                    icon: "success",
                    button: false,
                    timer: 2000,
                    });
                this.editToggle = 0
            } else {
                swal({
                    title : "개인 정보 수정에 실패 했습니다.",
                    text : "잠시 후 다시 시도해 주세요.",
                    icon: "error",
                    button: false,
                    timer: 2000,
                    });
            }
        }
    }
}
</script>
<style lang="scss" scope>
    .btn {
        height: 2rem;
    }
</style>