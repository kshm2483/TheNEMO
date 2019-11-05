const set = (name, token) => {
    sessionStorage.setItem(name, JSON.stringify(token))
}
const get = () => {
    return JSON.parse(sessionStorage.getItem('drf')).username
}
const destroy = () => {
    sessionStorage.removeItem("drf")
    sessionStorage.removeItem("token")
}
const check = () => {
    const key = sessionStorage.getItem("drf")
    return (key)? true: false
}
const checkStaff = () => {
    const key = JSON.parse(sessionStorage.getItem("drf"))
    return key.is_staff
}

export default {
    set,
    get,
    destroy,
    check,
    checkStaff
}
