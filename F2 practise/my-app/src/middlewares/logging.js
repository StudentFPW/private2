// export function logging(store) {
//     return function (next) {
//         return function (action) {
//             console.log(action);
//             return next(action);
//         }
//     }
// }

export const logging = store => next => action => {
    console.log(action);
    return next(action);
}