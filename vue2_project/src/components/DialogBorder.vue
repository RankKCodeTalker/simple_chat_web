<template>
  <div class="dialog-border" :class="isAI(id)">
    <pre class="dialog-text">{{ text }}</pre>
  </div>
</template>

<script>
  export default {
    name: 'DialogBorder',
    props: ['text', 'id'],
    components: {},
    data() {return{
    }},
    methods: {
      isAI(id) {
        if (id%2) return 'ai';
        else return 'human';
      }
    }
  }
</script>

<style scoped>
.dialog-border {
    margin: 5px;
    padding: 3px;
    border-radius: 5px;
    text-align: left;
}
.ai {
  background-color: rgb(121, 235, 229);
}
.human {
  background-color: rgb(233, 189, 157);
}
pre.dialog-text {
  font-size: 16px;
  white-space: pre-wrap; /*css-3*/
  white-space: -moz-pre-wrap; /*Mozilla,since1999*/
  white-space: -pre-wrap; /*Opera4-6*/
  white-space: -o-pre-wrap; /*Opera7*/
  word-wrap: break-word; /*InternetExplorer5.5+*/
}
</style>
