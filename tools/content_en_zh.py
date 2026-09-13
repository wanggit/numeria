"""English and Simplified Chinese content for the Numeria privacy policy.

Every fact asserted here is verifiable in the app source:
  * no networking code (only `url_launcher` opening external links)
  * `PrefsKeys` in lib/services/user_prefs.dart lists exactly the six
    locally-stored items described in the table below
  * calculator inputs are never persisted
  * one non-consumable `unlock_all` via StoreKit (lib/services/entitlement.dart)
"""

SUPPORT_URL = "https://github.com/wanggit/numeria/issues"
PAGES_URL = "https://wanggit.github.io/numeria/privacy/"

EN = {
    "code": "en",
    "html_lang": "en",
    "label": "English",
    "dir": "ltr",
    "doc_title": "Numeria — Privacy Policy",
    "h1": "Privacy Policy",
    "product": "<strong>Numeria: Finance Calculators</strong> &middot; version 1.0.0 &middot; iOS (iPhone)",
    "effective": "Effective date: 13 September 2026",
    "tldr_head": "In one sentence",
    "tldr": "Numeria collects nothing. There is no account, no advertising, no analytics and no "
            "server &mdash; every calculation happens entirely on your device, and the numbers you "
            "type are never stored or transmitted.",
    "blocks": [
        ("h2", "1. What we do not collect"),
        ("p", "Numeria contains no server component and issues no network requests of its own. "
              "We therefore cannot collect, and have never collected:"),
        ("ul", [
            "personal identifiers such as your name, email address, phone number or date of birth",
            "financial account details such as bank, card or brokerage account numbers",
            "precise or approximate location",
            "contacts, photos, health data, or any other content from your device",
            "usage analytics, behavioural profiles, or the advertising identifier (IDFA)",
        ]),
        ("p", "Because nothing is collected in the first place, there is nothing that could be "
              "shared with, sold to, or breached by a third party. The App Store privacy label for "
              "Numeria is <strong>&ldquo;Data Not Collected&rdquo;</strong>."),

        ("h2", "2. What is stored on your device"),
        ("p", "Numeria writes a small amount of data to your device&rsquo;s local preferences store "
              "so that it can remember your choices between launches. This data never leaves your "
              "device and is not readable by us:"),
        ("table", {
            "head": ["Stored item", "Why it exists"],
            "rows": [
                ["Identifiers of the last 10 calculators you opened",
                 "Populates the &ldquo;Recent&rdquo; list on the home screen"],
                ["Identifiers of calculators you marked as favourites",
                 "Populates your &ldquo;Favourites&rdquo; list"],
                ["Currency symbol preference",
                 "Formats monetary results the way you expect"],
                ["Theme preference (light, dark or system)",
                 "Applies your chosen appearance"],
                ["Language preference",
                 "Displays the interface in your language"],
                ["Unlock flag",
                 "Remembers that you purchased &ldquo;Unlock All&rdquo; so you are never asked to pay twice"],
            ],
        }),
        ("note", "<strong>The figures you enter are not saved.</strong> No calculator input, "
                 "intermediate value or result is written to disk or sent anywhere. Closing a "
                 "calculator discards whatever you typed into it."),

        ("h2", "3. Purchases"),
        ("p", "Numeria offers a single non-consumable in-app purchase, &ldquo;Unlock All "
              "Calculators&rdquo;. Payment is processed entirely by Apple through the App Store and "
              "StoreKit. We never see, receive or store your payment method, card number, Apple ID "
              "or purchase history."),
        ("p", "The only purchase-related datum the app keeps is the local unlock flag described "
              "above. When you use <em>Restore Purchases</em>, the app queries the App Store "
              "directly from your device; the response is used to set that flag and is not "
              "forwarded to us. Refunds are handled by Apple under its own policies."),

        ("h2", "4. Third parties"),
        ("p", "Numeria embeds no third-party SDKs &mdash; no advertising networks, no analytics "
              "providers, no social-media SDKs, no crash reporters. The only platform services it "
              "communicates with are:"),
        ("ul", [
            "Apple&rsquo;s App Store, solely to validate the in-app purchase, and",
            "your device&rsquo;s external browser, when you tap the <em>Support</em> or "
            "<em>Privacy Policy</em> links in Settings and the system opens that URL outside the app.",
        ]),

        ("h2", "5. About this web page"),
        ("p", "The app collects nothing, but this document is hosted on GitHub Pages so that the "
              "App Store has a URL to link to. When you load it, GitHub may record standard server "
              "log information &mdash; such as your IP address, browser type and request time "
              "&mdash; under <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\" rel=\"noopener\">GitHub&rsquo;s own privacy statement</a>. "
              "We do not receive or have access to those logs."),
        ("p", "This page loads no external fonts, scripts, stylesheets, images or trackers. The "
              "only thing it writes to your browser is your chosen language, so that the page "
              "reopens in the same language next time."),

        ("h2", "6. Children"),
        ("p", "Numeria is a general-purpose calculation tool with an age rating of 4+. It is not "
              "directed at children, and it collects no data from anyone &mdash; children included."),

        ("h2", "7. Data retention and deletion"),
        ("p", "There is no server-side copy of your data, so there is nothing for us to retain, "
              "export or delete. To remove every trace of data Numeria has written, simply delete "
              "the app: uninstalling erases the local preferences listed in section 2."),

        ("h2", "8. Your rights"),
        ("p", "Because Numeria holds no personal data about you, there is no personal data for us "
              "to disclose, correct, export or erase on request. Rights under the GDPR, the CCPA "
              "and similar regimes attach to personal data, and this app creates none. If you "
              "believe anything on this page is inaccurate, please tell us and we will correct it."),

        ("h2", "9. Changes to this policy"),
        ("p", "If a future version of Numeria changes anything described here &mdash; for example, "
              "if we added optional cloud sync or any networked feature &mdash; we will update this "
              "page, revise the effective date above, and disclose the change in the App Store "
              "release notes before that version ships."),

        ("h2", "10. Contact"),
        ("p", "Questions about this policy, or about the app: "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a>"),
        ("p", "Developer: <strong>wanggit</strong> (individual developer), publisher of "
              "<em>Numeria: Finance Calculators</em> on the App Store."),
    ],
    "disclaimer_head": "Not financial advice",
    "disclaimer": "Numeria produces arithmetic estimates for planning purposes. Its output is not "
                  "financial, tax, legal or investment advice, and it does not take your complete "
                  "circumstances into account. Consult a qualified professional before acting on "
                  "any figure the app shows you.",
}

ZH = {
    "code": "zh",
    "html_lang": "zh-Hans",
    "label": "简体中文",
    "dir": "ltr",
    "doc_title": "Numeria — 隐私政策",
    "h1": "隐私政策",
    "product": "<strong>Numeria：财务计算器</strong> &middot; 版本 1.0.0 &middot; iOS（iPhone）",
    "effective": "生效日期：2026 年 9 月 13 日",
    "tldr_head": "一句话结论",
    "tldr": "Numeria 不收集任何信息。没有账号、没有广告、没有统计分析、没有服务器——"
            "所有计算全部在你的设备上完成，你输入的数字既不会被保存，也不会被上传。",
    "blocks": [
        ("h2", "一、我们不收集哪些信息"),
        ("p", "Numeria 不含任何服务端组件，App 自身不发起网络请求。因此我们无法收集、"
              "也从未收集过下列信息："),
        ("ul", [
            "姓名、邮箱、电话号码、出生日期等个人身份信息",
            "银行账号、银行卡号、证券账户等金融账户信息",
            "精确或大致位置",
            "通讯录、照片、健康数据，或设备上的任何其他内容",
            "使用行为分析、用户画像，以及广告标识符（IDFA）",
        ]),
        ("p", "由于一开始就没有收集任何数据，也就不存在向第三方共享、出售，或被第三方"
              "泄露的可能。Numeria 在 App Store 的隐私标签为"
              "<strong>「不收集数据」（Data Not Collected）</strong>。"),

        ("h2", "二、哪些信息保存在你的设备上"),
        ("p", "为了在多次启动之间记住你的选择，Numeria 会向设备的本地偏好存储写入少量数据。"
              "这些数据不会离开你的设备，我们也无法读取："),
        ("table", {
            "head": ["保存的内容", "用途"],
            "rows": [
                ["你最近打开的 10 个计算器的标识符", "用于在首页显示「最近使用」列表"],
                ["你收藏的计算器标识符", "用于显示「收藏」列表"],
                ["货币符号偏好", "按你习惯的方式格式化金额结果"],
                ["主题偏好（浅色 / 深色 / 跟随系统）", "应用你选择的外观"],
                ["语言偏好", "以你选择的语言显示界面"],
                ["解锁标记", "记住你已购买「解锁全部」，避免重复付费"],
            ],
        }),
        ("note", "<strong>你输入的数值不会被保存。</strong>任何计算器的输入、中间值与结果"
                 "都不会写入磁盘，也不会发送到任何地方。关闭一个计算器，你刚才输入的内容"
                 "即被丢弃。"),

        ("h2", "三、购买"),
        ("p", "Numeria 仅提供一项非消耗型 App 内购买项目「解锁全部计算器」。支付完全由 Apple "
              "通过 App Store 与 StoreKit 处理，我们不会看到、接收或存储你的支付方式、"
              "银行卡号、Apple ID 或购买记录。"),
        ("p", "与购买相关、App 唯一保留的数据就是上文所述的本地解锁标记。当你点击"
              "<em>恢复购买</em>时，App 直接从你的设备向 App Store 查询，查询结果仅用于设置"
              "该标记，不会回传给我们。退款由 Apple 按其自身政策处理。"),

        ("h2", "四、第三方"),
        ("p", "Numeria 不集成任何第三方 SDK——没有广告联盟、没有统计服务商、没有社交平台 SDK、"
              "没有崩溃上报工具。它通信的对象仅限于："),
        ("ul", [
            "Apple 的 App Store，且仅用于校验 App 内购买；",
            "你设备的外部浏览器——当你在「设置」中点击<em>支持</em>或<em>隐私政策</em>链接时，"
            "由系统在 App 之外打开该网址。",
        ]),

        ("h2", "五、关于本网页"),
        ("p", "App 本身不收集任何信息，但本文件托管在 GitHub Pages 上，以便向 App Store 提供"
              "一个可访问的网址。你加载本页时，GitHub 可能依据"
              "<a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\" rel=\"noopener\">GitHub 自身的隐私声明</a>"
              "记录标准服务器日志信息，例如你的 IP 地址、浏览器类型与请求时间。"
              "我们不会收到、也无权访问这些日志。"),
        ("p", "本页不加载任何外部字体、脚本、样式表、图片或跟踪器。它写入你浏览器的唯一内容"
              "是你选择的语言，以便下次打开时仍显示同一语言。"),

        ("h2", "六、儿童"),
        ("p", "Numeria 是通用计算工具，年龄分级为 4+。它并非面向儿童设计，也不会收集任何人"
              "（包括儿童）的数据。"),

        ("h2", "七、数据留存与删除"),
        ("p", "服务端不存在你的任何数据副本，因此我们这边没有需要留存、导出或删除的内容。"
              "若希望彻底清除 Numeria 写入的数据，直接删除 App 即可：卸载会一并抹除第二节"
              "列出的全部本地偏好数据。"),

        ("h2", "八、你的权利"),
        ("p", "由于 Numeria 不持有任何关于你的个人数据，也就不存在可供我们依请求披露、更正、"
              "导出或删除的个人数据。GDPR、CCPA 等法规赋予的权利针对的是个人数据，"
              "而本 App 不产生任何个人数据。如果你认为本页任何表述有误，请告知我们，"
              "我们会更正。"),

        ("h2", "九、政策变更"),
        ("p", "如果 Numeria 的未来版本改变了本页所述的任何内容——例如新增可选的云同步或任何"
              "联网功能——我们会更新本页、修订上方的生效日期，并在该版本上架前于 App Store "
              "的更新说明中披露此项变更。"),

        ("h2", "十、联系我们"),
        ("p", "对本政策或本 App 有任何疑问，请在 "
              "<a href=\"" + SUPPORT_URL + "\" rel=\"noopener\">" + SUPPORT_URL + "</a> 提交 issue。"),
        ("p", "开发者：<strong>wanggit</strong>（个人开发者），App Store 上"
              "<em>Numeria：财务计算器</em>的发布者。"),
    ],
    "disclaimer_head": "不构成专业建议",
    "disclaimer": "Numeria 输出的是用于规划的算术估算值，不构成财务、税务、法律或投资建议，"
                  "也无法涵盖你的完整实际情况。在依据 App 显示的任何数字采取行动前，"
                  "请咨询具备资质的专业人士。",
}
