/**
     *  存放 ** 数据
     * **/

// initial state
const state = {
    missed_orders: {
        missed_orders: [],
    }
}

// getters
const getters = {}

// actions
const actions = {}

// mutations
const mutations = {
    setOrders(state, missed_orders) { //设置参数
        state.missed_orders = missed_orders;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}