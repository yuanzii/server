/**
     *  存放 ** 数据
     * **/

// initial state
const state = {
    list: {
        list: '',
    }
}

// getters
const getters = {}

// actions
const actions = {}

// mutations
const mutations = {
    setPrint(state, list) { //设置参数
        state.list = list;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}