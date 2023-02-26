<template>
  <div class="home">
    <el-container>
      <el-main id="el-main" ref="main">
        <el-row v-for="(text, id) of dialogs" :key="id">
          <dialog-border :text="text" :id="id"></dialog-border>
        </el-row>
      </el-main>
      <el-footer id="el-footer">
        <el-row>
          <el-col :span="20"><el-input v-model="input" placeholder="请输入内容"></el-input></el-col>
          <el-col :span="4"><el-button type="primary" @click="ask()">发送</el-button></el-col>
        </el-row>
      </el-footer>
    </el-container>
  </div>
</template>

<style scoped>
#el-main {
  margin-bottom: 50px;
}
#el-footer {
  position: fixed;
  left: 0px;
  bottom: 0px;
  width: 100%;
  padding-top: 10px;
  background: white;
}
</style>

<script>
import { back_url_prefix } from '../constant'
import axios from 'axios'
import {Button, Container, Footer, Input, Main, Row} from 'element-ui'
import DialogBorder from '../components/DialogBorder.vue'

// let domMain = document.getElementById('el-main')

export default {
  name: 'home',
  data() { return {
    dialogs: [],
    prompt: '',
    hasProblem: false,
    input: '',
  }},
  // computed: {
  //   buttonText() {
  //     if (hasProblem) return '重发';
  //     else return '发送';
  //   }
  // },
  components: {Button, Container, Footer, Input, Main, Row, DialogBorder},
  methods: {
    ask() {
      if (this.hasProblem) {
        this.dialogs.pop();
        axios.post(back_url_prefix+'/ask',{
          prompt: this.prompt
        }).then(resp => {
          var code = resp.data.code;
          var text = resp.data.text;
          this.dialogs.push(text);
          if (code == 0) {
            this.prompt += text+'\n';
            this.hasProblem = false;
          }
        })
      }
      else {
        if (this.input.length === 0) {
          alert('输入不能为空！');
          return;
        }
        this.dialogs.push(this.input);
        this.prompt += '问：'+this.input+'\n答：';
        this.input = ''
        this.scrollToBottom();
        axios.post(back_url_prefix+'/ask',{
          prompt: this.prompt
        }).then(resp => {
          var code = resp.data.code;
          var text = resp.data.text;
          this.dialogs.push(text);
          if (code == 0) {
            this.prompt += text+'\n';
            this.scrollToBottom();
          } else {
            this.hasProblem = true;
          }
        })
      }
    },
    scrollToBottom() {
      this.$nextTick(() => {
        var height = document.getElementById('el-main').clientHeight;
        console.log(height);
        setTimeout(window.scroll({ top: height, left: 0, behavior: 'smooth' }), 500);
      })
    }
  },
  // mounted() {
  //   // let height = this.$refs.main.style.height; // 100px
  //   // let height = window.getComputedStyle(this.$refs.main).height; // 100px
  //   // let height= this.$refs.main.offsetHeight;  //100
  //   // console.log(height)
  //   // var t = document.getElementById('el-main').clientHeight;
  //   // window.scroll({ top: domMain.clientHeight, left: 0, behavior: 'smooth' });
  // }
}
</script>
