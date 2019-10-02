const set = (name, token) => {
    sessionStorage.setItem(name, JSON.stringify(token))
}
const destroy = () => {
    sessionStorage.removeItem("drf")
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
    destroy,
    check,
    checkStaff
}